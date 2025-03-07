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
        
        # Update submodule (pull latest changes)
        submodule.update(init=True, recursive=False)
        
        # Refresh the submodule reference and get the new commit hash from its repo
        new_hash = submodule.module().head.commit.hexsha[:7]  # Use only first 7 digits
        
        # Stage the updated pointer in the parent repository
        repo.git.add(submodule.path)
        commit_message = f"chore(submodule): update {submodule_name} to {new_hash}"
        
        # Check if there is a diff in the staged pointer compared to HEAD
        diff = repo.git.diff('HEAD', submodule.path)
        if diff:
            try:
                repo.index.commit(commit_message)
                print(commit_message)
                repo.remote().push()
                print(f"Pushed update for {submodule_name}")
            except git.GitCommandError as e:
                print(f"Failed to commit/push for {submodule_name}: {e}")
        else:
            print(f"No changes detected for submodule: {submodule_name}")

if __name__ == "__main__":
    update_submodules(".")
