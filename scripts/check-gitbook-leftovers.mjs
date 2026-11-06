import fs from 'node:fs';
import path from 'node:path';

const root = 'src/content/docs';
const hits = [];

function walk(dir) {
	for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
		const full = path.join(dir, entry.name);
		if (entry.isDirectory()) {
			walk(full);
			continue;
		}
		const text = fs.readFileSync(full, 'utf8');
		if (text.includes('{%')) hits.push(full);
	}
}

walk(root);
if (hits.length) {
	console.error('GitBook tags are still in:');
	for (const file of hits) console.error(`  ${file}`);
	process.exit(1);
}
