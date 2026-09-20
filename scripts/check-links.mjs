// SPDX-License-Identifier: MIT
// Checks local inline Markdown file links; does not validate URL or heading anchors.
import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { dirname, join, relative, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(process.argv[2] || join(dirname(fileURLToPath(import.meta.url)), '..'));
let checked = 0;
const missing = [];

function walk(directory) {
  for (const item of readdirSync(directory, { withFileTypes: true })) {
    if (['.git', 'node_modules', '.agents'].includes(item.name) || item.name.startsWith('.asset-validation-')) continue;
    const file = join(directory, item.name);
    if (item.isDirectory()) walk(file);
    else if (item.isFile() && item.name.endsWith('.md')) check(file);
  }
}

function check(file) {
  let fence;
  for (const [index, line] of readFileSync(file, 'utf8').split(/\r?\n/).entries()) {
    const marker = line.match(/^\s*(`{3,}|~{3,})(.*)$/);
    if (marker) {
      if (!fence) fence = marker[1];
      else if (marker[1][0] === fence[0] && marker[1].length >= fence.length && !marker[2].trim()) fence = undefined;
      continue;
    }
    if (fence) continue;
    for (const match of line.matchAll(/\[[^\]\n]*\]\((?:<([^>\n]+)>|([^\s)]+))(?:\s+"[^"]*")?\)/g)) {
      const href = match[1] || match[2];
      if (/^(?:[a-z][a-z\d+.-]*:|#|\/)/i.test(href)) continue;
      const path = decodeURIComponent(href.split(/[?#]/, 1)[0]);
      if (!path) continue;
      checked += 1;
      const target = resolve(dirname(file), path);
      if (!existsSync(target) || !statSync(target).isFile()) {
        missing.push(`${relative(root, file)}:${index + 1}: ${href}`);
      }
    }
  }
}

walk(root);
if (missing.length) {
  console.error(`Missing local Markdown targets:\n${missing.join('\n')}`);
  process.exitCode = 1;
} else {
  console.log(`Checked ${checked} local Markdown file links.`);
}
