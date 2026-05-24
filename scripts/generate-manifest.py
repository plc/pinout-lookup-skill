#!/usr/bin/env python3
"""
Generate components.json manifest from pinout markdown files.

Walks component directories (boards/, displays/, sensors/, etc.) and extracts
metadata from each .md file to build a searchable manifest.
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Set


# Directories to skip during component discovery
SKIP_DIRS = {'.github', 'scripts', '.git', 'node_modules', '__pycache__'}

# Common words to exclude from auto-generated keywords
COMMON_WORDS = {
    'the', 'and', 'for', 'with', 'this', 'that', 'from', 'have', 'has',
    'are', 'was', 'were', 'been', 'being', 'into', 'through', 'during',
    'before', 'after', 'above', 'below', 'between', 'under', 'again',
    'further', 'then', 'once', 'also', 'can', 'each', 'not', 'when',
    'includes', 'directly', 'onto', 'separate', 'via', 'using', 'used',
    'use', 'per', 'both', 'some', 'any', 'all', 'its', 'may', 'but',
    'operation', 'optional', 'onboard',
}


def extract_heading(content: str) -> str:
    """Extract the first H1 heading from markdown content."""
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('# '):
            return line[2:].strip()
    return ""


def extract_description(content: str) -> str:
    """Extract the first non-empty line after the Source: line.

    Stop looking if we hit a heading or code block - boards don't have descriptions.
    """
    lines = content.split('\n')
    found_source = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('Source:') or stripped.startswith('Sources:'):
            found_source = True
            continue
        if found_source:
            # Stop if we hit a heading or code block
            if stripped.startswith('#') or stripped.startswith('```'):
                return ""
            # Skip list items
            if stripped.startswith('-') or stripped.startswith('*'):
                continue
            # Return the first meaningful line
            if stripped:
                return stripped

    return ""


def detect_interfaces(content: str, component_type: str) -> List[str]:
    """Detect communication interfaces from content."""
    interfaces = set()
    content_lower = content.lower()

    if component_type == 'board':
        # For boards, parse the Bus Defaults section
        if 'bus defaults' in content_lower:
            bus_section = content[content_lower.find('bus defaults'):]
            if 'i2c' in bus_section.lower():
                interfaces.add('I2C')
            if 'spi' in bus_section.lower():
                interfaces.add('SPI')
            if 'uart' in bus_section.lower():
                interfaces.add('UART')
    else:
        # For peripherals, scan headers and content
        if re.search(r'\bi2c\b', content_lower):
            interfaces.add('I2C')
        if re.search(r'\bspi\b', content_lower):
            interfaces.add('SPI')
        if re.search(r'\buart\b', content_lower):
            interfaces.add('UART')
        if re.search(r'\bgpio\b', content_lower):
            interfaces.add('GPIO')

    return sorted(list(interfaces))


def generate_keywords(filename: str, name: str, description: str) -> List[str]:
    """Generate keywords from filename, name, and description."""
    keywords = set()

    # Extract from filename (without extension, split on dashes and underscores)
    base_name = Path(filename).stem
    for part in re.split(r'[-_]', base_name):
        if part:
            keywords.add(part.lower())

    # Extract from name
    for word in re.split(r'[\s\-_/]+', name):
        # Remove punctuation and convert to lowercase
        word = re.sub(r'[^\w]', '', word).lower()
        if word and word not in COMMON_WORDS:
            keywords.add(word)

    # Extract from description
    for word in re.split(r'[\s\-_/,.:;]+', description):
        # Remove punctuation and convert to lowercase
        word = re.sub(r'[^\w]', '', word).lower()
        # Skip short words and common words
        if len(word) >= 3 and word not in COMMON_WORDS:
            keywords.add(word)

    return sorted(list(keywords))


def process_component_file(filepath: Path, repo_root: Path) -> Dict:
    """Process a single component markdown file and extract metadata."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get relative path from repo root
    relative_path = filepath.relative_to(repo_root)

    # Determine component type from directory name (singularize)
    component_type = filepath.parent.name
    if component_type.endswith('s'):
        component_type = component_type[:-1]

    # Extract metadata
    name = extract_heading(content)
    description = extract_description(content)
    interfaces = detect_interfaces(content, component_type)
    keywords = generate_keywords(filepath.name, name, description)

    return {
        'file': str(relative_path).replace('\\', '/'),  # Normalize path separators
        'name': name,
        'type': component_type,
        'description': description,
        'interfaces': interfaces,
        'keywords': keywords
    }


def find_component_directories(repo_root: Path) -> List[Path]:
    """Find all directories that contain component .md files."""
    component_dirs = []

    for item in repo_root.iterdir():
        if not item.is_dir():
            continue
        if item.name in SKIP_DIRS:
            continue
        if item.name.startswith('.'):
            continue

        # Check if directory contains any .md files (excluding known non-component files)
        md_files = list(item.glob('*.md'))
        if md_files:
            # Filter out template and doc files
            component_files = [
                f for f in md_files
                if f.name not in {
                    'pinout_template.md', 'WIRING_FORMAT.md',
                    'CONTRIBUTING.md', 'CLAUDE.md', 'README.md',
                    'CHANGELOG.md', 'LICENSE.md'
                }
            ]
            if component_files:
                component_dirs.append(item)

    return sorted(component_dirs)


def generate_manifest(repo_root: Path) -> Dict:
    """Generate the components manifest."""
    components = []

    # Find all component directories
    component_dirs = find_component_directories(repo_root)

    print(f"Found {len(component_dirs)} component directories:")
    for dir_path in component_dirs:
        print(f"  - {dir_path.name}/")
    print()

    # Process each component file
    for dir_path in component_dirs:
        md_files = sorted(dir_path.glob('*.md'))

        for filepath in md_files:
            # Skip template and documentation files
            if filepath.name in {
                'pinout_template.md', 'WIRING_FORMAT.md',
                'CONTRIBUTING.md', 'CLAUDE.md', 'README.md',
                'CHANGELOG.md', 'LICENSE.md'
            }:
                continue

            try:
                component = process_component_file(filepath, repo_root)
                components.append(component)
                print(f"Processed: {component['file']} ({component['type']})")
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

    return {'components': components}


def main():
    """Main entry point."""
    # Get repo root (parent of scripts directory)
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent

    print(f"Generating manifest from: {repo_root}\n")

    # Generate manifest
    manifest = generate_manifest(repo_root)

    # Write to components.json
    output_path = repo_root / 'components.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, sort_keys=True, ensure_ascii=False)
        f.write('\n')  # Add trailing newline

    print(f"\nManifest generated: {output_path}")
    print(f"Total components: {len(manifest['components'])}")

    # Summary by type
    types = {}
    for component in manifest['components']:
        comp_type = component['type']
        types[comp_type] = types.get(comp_type, 0) + 1

    print("\nBreakdown by type:")
    for comp_type, count in sorted(types.items()):
        print(f"  {comp_type}: {count}")


if __name__ == '__main__':
    main()
