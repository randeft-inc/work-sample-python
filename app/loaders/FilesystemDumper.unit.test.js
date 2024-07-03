import fs from 'fs';
import path from 'path';
import FilesystemDumper from './FilesystemDumper.js';

const instance = new FilesystemDumper();

describe('load', () => {
  const filePath = './output/file_dumper_test.txt';
  const content = 'Some content';

  test('writes content to output folder', () => {
    instance.load([
      {
        filename: path.basename(filePath),
        content,
      },
    ]);
    const writtenData = fs.readFileSync(filePath, 'utf-8');
    expect(writtenData).toEqual(content);
  });

  afterAll(() => {
    fs.unlinkSync(filePath);
  });
});
