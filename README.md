# NFIQ 2 <img src="cmake/nist_itl_two_color.svg" align="right" alt="NIST Information Technology Laboratory" style="width:250px;" />

[![Download Latest Version](https://img.shields.io/badge/download-v2.3-informational)](https://github.com/usnistgov/NFIQ2/releases)
[![Build Libraries and CLI + Run CTS](https://github.com/usnistgov/NFIQ2/actions/workflows/build-member.yml/badge.svg)](https://github.com/usnistgov/NFIQ2/actions/workflows/build-member.yml)
[![Frequently Asked Questions](https://img.shields.io/badge/wiki-frequently%20asked%20questions-informational)](https://github.com/usnistgov/NFIQ2/wiki/Frequently-Asked-Questions)

About
-----
[National Institute of Standards and Technology (NIST)](https://www.nist.gov)
Fingerprint Image Quality (NFIQ) is software that links image
quality of optical and ink plain impression 500 pixel per inch fingerprints to operational
recognition performance. This allows quality values to be tightly defined and
then numerically calibrated, which in turn allows for the standardization needed
to support a worldwide deployment of fingerprint sensors with
universally-interpretable image qualities. NFIQ 2 quality features are formally
standardized as part of
[ISO/IEC 29794-4](http://www.iso.org/iso/catalogue_detail.htm?csnumber=62791).
This repository serves as a formally-recognized reference implementation of the
2024 international standard.

Download
--------
Pre-built versions of the NFIQ 2 library and standalone executable for many
platforms are available to download on the
[GitHub Releases](https://github.com/usnistgov/NFIQ2/releases) page.

Dependencies
------------

Building the NFIQ 2 library requires the following dependencies, included in
this repository as git submodules:

 * [digestpp](https://github.com/kerukuro/digestpp) ([public domain license](https://github.com/kerukuro/digestpp/blob/master/LICENSE))
 * [FingerJetFX OSE](https://github.com/FingerJetFXOSE/FingerJetFXOSE) ([LGPLv3 license](https://github.com/FingerJetFXOSE/FingerJetFXOSE/blob/master/COPYRIGHT.txt))
 * [OpenCV](https://github.com/opencv/opencv) ([Apache 2 License](https://github.com/opencv/opencv/blob/master/LICENSE))

If building the standalone command-line executable, additional dependencies are
required, included in this repository as git submodules:

 * [Biometric Evaluation Framework](https://github.com/usnistgov/libbiomeval) ([public domain license](https://github.com/usnistgov/libbiomeval/blob/master/LICENSE.md))
   * Requires other non-bundled dependencies, please see the [README](https://github.com/usnistgov/libbiomeval/blob/master/README.md).
 * [NIST Fingerprint Image Resampler](https://github.com/usnistgov/nfir) (public domain license)
   * Requires [OpenCV](https://github.com/opencv/opencv), which is required by NFIQ 2 library.

Quick Build: Library
--------------------

> [!IMPORTANT]
> Unless you are *actively developing* code for NFIQ 2, we **highly** suggest
> you download from [Releases](https://github.com/usnistgov/NFIQ2/releases)
> instead of attempting to compile.

> [!NOTE]
> You must *recursively* clone the repository to retrieve git submodules
> (i.e., do **not** use the GitHub ZIP file download).

```bash
git clone --recursive https://github.com/usnistgov/NFIQ2.git
cd NFIQ2
mkdir build
cd build
cmake .. -DBUILD_NFIQ2_CLI=OFF
cmake --build .
```

Quick Build: Library + Command-line Interface
---------------------------------------------

> [!IMPORTANT]
> Unless you are *actively developing* code for NFIQ 2, we **highly** suggest
> you download from [Releases](https://github.com/usnistgov/NFIQ2/releases)
> instead of attempting to compile.

> [!NOTE]
> You must *recursively* clone the repository to retrieve git submodules
> (i.e., do **not** use the GitHub ZIP file download).

```bash
git clone --recursive https://github.com/usnistgov/NFIQ2.git
cd NFIQ2
mkdir build
cd build
cmake ..
cmake --build .
```
