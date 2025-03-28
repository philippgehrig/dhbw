# ITA22 Lecture Materials and Repositories

This repository contains the lecture materials and repositories for ITA22 courses at DHBW Stuttgart. It includes several submodules for different courses, each with its own repository. All classes were completed between October 2022 and September 2025.

## Cloning the Repository

To clone this repository along with its submodules, use the following command:

```sh
git clone --recursive https://github.com/philippgehrig/dhbw.git
```

If you have already cloned the repository without the `--recursive` option, you can initialize and update the submodules with the following commands:

```sh
git submodule init
git submodule update
```

Alternatively, you can use a single command to clone and update the submodules:

```sh
git submodule update --init --recursive
```

## updating submodules

There is a Python Script to update all the submodules. To use it you need to create a virtual enviroement

```bash
python3 -m venv {venv_name} && source {venv_name}/bin/activate && pip install gitpython configparser  
```

Then you can run the script with

```bash
python3 update-submodules.py
```

## Submodules

The repository includes the following submodules:

- `T3-3101-Studienarbeit`
- `T3INF1001-Mathematik-I`
- `T3INF1002-Theoretische-Informatik-I`
- `T3INF1003-Theoretische-Informatik-II`
- `T3INF1004-Software-Engineering`
- `T3INF1005-Key-Qualifications`
- `T3INF1006-Teschnische-Informatik-I`
- `T3INF2001-Mathematik-II`
- `T3INF2002-Compilerbau`
- `T3INF2002-Theoretische-Informatik-III`
- `T3INF2003-Web-Engineering`
- `T3INF2004-Datenbanken-I`
- `T3INF2005-Technische-Informatik-II`
- `T3INF3001-Advanced-Software-Engineering`
- `T3INF3002-IT-Security`
- `T3INF4252-Messdatenerfassung`
- `T3INF4308-GPS`
- `T3INF4309-FAS`
- `T3INF4901-Autonomes-Fahren`
- `T3INF4902-DevOps`
- `T3300-Thesis`

## Contributing

Please fork this repository and submit pull requests for any improvements or fixes. Make sure to update the submodules if needed.
