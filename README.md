# wallflower

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8d1a42e7b40947b18793150b16825e14)](https://www.codacy.com/manual/KawashimaHirotaka/wallflower?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=khirotaka/wallflower&amp;utm_campaign=Badge_Grade)
[![Anaconda-Server Badge](https://anaconda.org/khirotaka/wallflower/badges/version.svg)](https://anaconda.org/khirotaka/wallflower)
[![Anaconda-Server Badge](https://anaconda.org/khirotaka/wallflower/badges/latest_release_date.svg)](https://anaconda.org/khirotaka/wallflower)
[![Anaconda-Server Badge](https://anaconda.org/khirotaka/wallflower/badges/latest_release_relative_date.svg)](https://anaconda.org/khirotaka/wallflower)
[![Anaconda-Server Badge](https://anaconda.org/khirotaka/wallflower/badges/platforms.svg)](https://anaconda.org/khirotaka/wallflower)
[![Anaconda-Server Badge](https://anaconda.org/khirotaka/wallflower/badges/license.svg)](https://anaconda.org/khirotaka/wallflower)
[![Anaconda-Server Badge](https://anaconda.org/khirotaka/wallflower/badges/downloads.svg)](https://anaconda.org/khirotaka/wallflower)
[![Anaconda-Server Badge](https://anaconda.org/khirotaka/wallflower/badges/installer/conda.svg)](https://conda.anaconda.org/khirotaka)

## Installation 🖥 ← 📦
Conda package is now available!
you just execute this command if you want to install packages.

```shell script
conda install -c khirotaka wallflower
```

## Requirements 📝
This packages depends on those packages and systems.
 
*   Python 3.6 or later
*   NumPy
*   SciPy

## 🛠 Build Package 📦
If you want to build this package on your machine, you just follow this order.

1.  clone this repository
2.  move `wallflower/` directory
3.  `conda-build wallflower`

```shell script
git clone https://github.com/khirotaka/wallflower.git
cd wallflower/
conda-build wallflower
```

Typically, built package is saved on
`~/anaconda3/envs/ENVIRONMENT_NAME/conda-bld/PLATFORM/wallflower-VERSION-py36_0.tar.bz2`

if you want to upload your built packages to anaconda cloud, execute this command.

```shell script
anaconda upload ~/anaconda3/envs/ENVIRONMENT_NAME/conda-bld/PLATFORM/wallflower-VERSION-py36_0.tar.bz2
```

finally, you can get packages from your channel of  anaconda cloud.

### Optional 🛠
Convert your package for all platforms📦

```shell script
conda-convert --platform all ~/anaconda3/envs/ENVIRONMENT_NAME/conda-bld/PLATFORM/wallflower-VERSION-py36_0.tar.bz2 -o packages/
```
## Usage
