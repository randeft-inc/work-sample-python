import ETLPipeline from './pipelines/ETLPipeline';
import DataExtractor from './extractors/DataExtractor';
import ExcelConverter from './transformers/ExcelConverter';
import FilesystemDumper from './loaders/FilesystemDumper';

const pipeline = new ETLPipeline({
  extractor: new DataExtractor(),
  transformer: new ExcelConverter(),
  loader: new FilesystemDumper(),
});

pipeline.perform();
