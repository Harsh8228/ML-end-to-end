from setuptools import find_packages, setup

def get_requirements(file_path: str) -> list[str]:
    requirements = []
    with open(file_path, "r") as f:
        for line in f:
            req = line.strip()
            if req and not req.startswith("#") and req != "-e .":
                requirements.append(req)
    return requirements

setup(
    name="ml end to end",
    version="0.1",
    author="Harsh",
    email="harsh480vardhan@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)