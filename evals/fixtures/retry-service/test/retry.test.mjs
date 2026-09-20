// SPDX-License-Identifier: MIT
import assert from 'node:assert/strict';
import test from 'node:test';
import { retry } from '../src/retry.mjs';

test('returns the first successful result without another attempt', async () => {
  const seen = [];
  const result = await retry(async (attempt) => {
    seen.push(attempt);
    return 'ready';
  });
  assert.equal(result, 'ready');
  assert.deepEqual(seen, [1]);
});

test('the default permits two failures before a successful third attempt', async () => {
  const seen = [];
  const result = await retry(async (attempt) => {
    seen.push(attempt);
    if (attempt < 3) throw new Error('temporary failure');
    return 'ready';
  });
  assert.equal(result, 'ready');
  assert.deepEqual(seen, [1, 2, 3]);
});
