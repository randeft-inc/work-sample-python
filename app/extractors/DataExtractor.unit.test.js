import DataExtractor from './DataExtractor.js';

const instance = new DataExtractor();

describe('extract', () => {
  const subject = instance.extract();

  test('returns 2 items', () => {
    const itemsCount = subject.length;
    expect(itemsCount).toEqual(2);
  });

  test('items have expected basenames', () => {
    const basenames = subject.map((data) => data.basename);
    expect(basenames).toEqual(['sample_1', 'sample_2']);
  });

  test('items have expected contents', () => {
    const excerpts = subject.map((data) => data.content.slice(0, 8));
    expect(excerpts).toEqual(['2006/12/', '[Header]']);
  });
});
