# extract-ogg

## Introduction
This Python repository offers a tool for extracting embedded OGG files from RIFF/WAVE files. The utility, `RIFFOgg.py`, simplifies the process, enabling users to effortlessly extract OGG audio from RIFF/WAVE files.

## Installation
This tool requires Python to be installed on your system. If you haven't installed Python yet, download and install it from [Python's official website](https://www.python.org/downloads/).

Once you have Python installed, download this repository to your local machine.

## Usage
Navigate to the directory containing the repository and run the script with the following command:

```bash
python RIFFOgg.py input.wav output.ogg
```

Replace `input.wav` with the path to your RIFF/WAVE file containing embedded OGG audio, and `output.ogg` with the desired filename for the extracted OGG file.

## Example
For instance, if you have a RIFF/WAVE file named `audio.wav` and you want to extract the embedded OGG audio to a file named `extracted_audio.ogg`, you would run:

```bash
python RIFFOgg.py audio.wav extracted_audio.ogg
```

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository.

If you would like to contribute code, fork the repository, create a new branch, commit your changes, and open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
