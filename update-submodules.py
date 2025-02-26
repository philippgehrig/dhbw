import git
import configparser

def update_submodules(repo_path):
    repo = git.Repo(repo_path)
    config = configparser.ConfigParser()
    
    gitmodules_path = f"{repo_path}/.gitmodules"
    config.read(gitmodules_path)
    
    submodules = [section.split('"')[1] for section in config.sections() if section.startswith("submodule")]
    
    for submodule_name in submodules:
        submodule = repo.submodule(submodule_name)
        print(f"Updating submodule: {submodule_name}")
        
        submodule.update(init=True, recursive=False)
        # Refresh the submodule reference and get the new commit hash from its repo
        new_hash = submodule.module().head.commit.hexsha
        
        repo.git.add(submodule.path)
        commit_message = f"chore(submodule): update {submodule_name} to {new_hash}"
        repo.index.commit(commit_message)
        print(commit_message)
    
    repo.remote().push()
    print("Pushed updated submodule references to remote repository.")

if __name__ == "__main__":
    update_submodules(".")