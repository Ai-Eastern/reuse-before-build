// SPDX-License-Identifier: MIT
export async function retry(operation, { attempts = 3 } = {}) {
  if (!Number.isInteger(attempts) || attempts < 1) {
    throw new RangeError('attempts must be a positive integer');
  }

  for (let attempt = 1; attempt <= attempts; attempt += 1) {
    try {
      return await operation(attempt);
    } catch (error) {
      if (attempt === attempts) throw error;
    }
  }
}
