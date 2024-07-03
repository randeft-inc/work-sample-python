import fs from 'fs';
import ExcelConverter from './ExcelConverter.js';

const instance = new ExcelConverter({});

describe('transform', () => {
  describe('with type 1 data', () => {
    const basename = 'type_1';
    const content = fs.readFileSync('./raw_data/sample_1.dat', 'utf-8');
    const transformed = instance.transform([{ basename, content }]);

    test('generates the expected filename', () => {
      expect(transformed[0].filename).toEqual('type_1.xlsx');
    });

    test('generates the expected content', () => {
      // for simplicity we only verify the content length
      expect(transformed[0].content.length).toEqual(151141);
    });
  });

  describe('with type 2 data', () => {
    const basename = 'type_2';
    const content = fs.readFileSync('./raw_data/sample_2.dat', 'utf-8');
    const transformed = instance.transform([{ basename, content }]);

    test('generates the expected filename', () => {
      expect(transformed[0].filename).toEqual('type_2.xlsx');
    });

    test('generates the expected content', () => {
      // for simplicity we only verify the content length
      expect(transformed[0].content.length).toEqual(84105);
    });
  });
});
