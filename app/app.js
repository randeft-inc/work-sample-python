import ETLPipeline from './pipelines/ETLPipeline.js';
import DataExtractor from './extractors/DataExtractor.js';
import ExcelConverter from './transformers/ExcelConverter.js';
import FilesystemDumper from './loaders/FilesystemDumper.js';

const pipeline = new ETLPipeline({
  extractor: new DataExtractor(),
  transformer: new ExcelConverter(),
  loader: new FilesystemDumper(),
});

pipeline.perform();
