import * as XLSX from 'xlsx/xlsx';

function ExcelConverter() {
  this.transform = function transform(data) {
    return data.map(({ basename, content }) => ({
      filename: `${basename}.xlsx`,
      content: this.convertToExcel(content),
    }));
  };

  this.convertToExcel = function convertToExcel(content) {
    const { separator, preprocessedContent } = this.preprocessContent(content);
    const wb = XLSX.read(preprocessedContent, { type: 'string', separator });
    return XLSX.write(wb, { bookType: 'xlsx', type: 'binary' });
  };

  this.preprocessContent = function preprocessContent(content) {
    const {
      separator,
      mustMergeSeparators,
      linesToSkip,
    } = this.options(content);
    let preprocessedContent = content.split('\n').slice(linesToSkip).join('\n');
    if (mustMergeSeparators) {
      const leadingSeparatorRegExp = new RegExp(`\n${separator}`, 'g');
      preprocessedContent = preprocessedContent
        .replaceAll(`${separator}${separator}`, separator) // merge consecutive separators
        .replaceAll(leadingSeparatorRegExp, '\n'); // remove leading separator
    }
    return { separator, preprocessedContent };
  };

  this.options = function options(content) {
    // Simplistic heuristic to classify two types of files
    if (content.includes('[Data]')) {
      return { separator: ',', mustMergeSeparators: false, linesToSkip: 30 };
    }
    return { separator: ' ', mustMergeSeparators: true, linesToSkip: 2 };
  };
}

export default ExcelConverter;
