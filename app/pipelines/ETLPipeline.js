function ETLPipeline({ extractor, transformer, loader }) {
  this.extractor = extractor;
  this.transformer = transformer;
  this.loader = loader;

  this.perform = function perform() {
    const extractedData = this.extractor.extract();
    const transformedData = this.transformer.transform(extractedData);
    this.loader.load(transformedData);
  };
}

export default ETLPipeline;
