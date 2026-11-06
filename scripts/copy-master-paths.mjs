import fs from 'node:fs';
import path from 'node:path';

const dist = 'dist';
const files = [];

function walk(dir) {
	for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
		const full = path.join(dir, entry.name);
		const rel = path.relative(dist, full);
		if (rel === 'master' || rel.startsWith(`master${path.sep}`)) continue;
		if (entry.isDirectory()) {
			walk(full);
			continue;
		}
		if (entry.name.endsWith('.html') || entry.name.startsWith('llms')) {
			files.push(full);
		}
	}
}

walk(dist);
for (const file of files) {
	const dest = path.join(dist, 'master', path.relative(dist, file));
	fs.mkdirSync(path.dirname(dest), { recursive: true });
	fs.copyFileSync(file, dest);
}
console.log(`copied ${files.length} html/llms files under /master`);
