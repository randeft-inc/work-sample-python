import { writeFileSync } from 'fs';

const OUTPUT_FOLDER = './output';

function FilesystemDumper() {
  this.load = function load(data) {
    data.forEach(({ filename, content }) => {
      writeFileSync(`${OUTPUT_FOLDER}/${filename}`, content, 'binary');
    });
  };
}

export default FilesystemDumper;
