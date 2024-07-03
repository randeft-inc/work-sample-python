import jest from 'jest-mock';
import ETLPipeline from './ETLPipeline.js';

const extract = jest.fn(() => 'extracted');
const transform = jest.fn(() => 'transformed');
const load = jest.fn();

const instance = new ETLPipeline({
  extractor: { extract },
  transformer: { transform },
  loader: { load },
});

describe('perform', () => {
  expect(extract).not.toHaveBeenCalled();
  expect(transform).not.toHaveBeenCalled();
  expect(load).not.toHaveBeenCalled();

  instance.perform();

  test('calls extract on the extractor', () => {
    expect(extract).toHaveBeenCalled();
  });

  test('calls transfrom on the transformer', () => {
    expect(transform).toHaveBeenCalled();
  });

  test('calls load on the loader', () => {
    expect(load).toHaveBeenCalled();
  });

  test('passes extracted data to the transformer', () => {
    expect(transform).toHaveBeenCalledWith('extracted');
  });

  test('passes transformed data to the loader', () => {
    expect(load).toHaveBeenCalledWith('transformed');
  });
});
