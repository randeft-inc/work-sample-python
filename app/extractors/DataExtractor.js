import { readdirSync, readFileSync } from 'fs';

const INPUT_FOLDER = './raw_data/';

function DataExtractor() {
  // For this sample, the extractor reads files from the local disk.
  // In practice, it would get data from an external system.

  this.extract = function extract() {
    const filenames = readdirSync(INPUT_FOLDER);
    return filenames.map((filename) => ({
      basename: filename.replace(/\..*/, ''),
      content: readFileSync(`${INPUT_FOLDER}/${filename}`, 'utf-8'),
    }));
  };
}

export default DataExtractor;
