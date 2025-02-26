import git
import configparser

def update_submodules(repo_path):
    repo = git.Repo(repo_path)
    config = configparser.ConfigParser()
    
    gitmodules_path = f"{repo_path}/.gitmodules"
    config.read(gitmodules_path)
    
    submodules = [section.split('"')[1] for section in config.sections() if section.startswith("submodule")]
    
    # Record the HEAD commit before updating submodules
    original_head = repo.head.commit.hexsha
    
    for submodule_name in submodules:
        submodule = repo.submodule(submodule_name)
        print(f"Updating submodule: {submodule_name}")
        
        submodule.update(init=True, recursive=False)
        # Refresh the submodule reference and get the new commit hash from its repo
        new_hash = submodule.module().head.commit.hexsha
        
        # Stage the updated pointer in the parent repository
        repo.git.add(submodule.path)
        commit_message = f"chore(submodule): update {submodule_name} to {new_hash}"
        
        # Only commit if there is a change to commit
        try:
            repo.index.commit(commit_message)
            print(commit_message)
        except git.GitCommandError as e:
            # This indicates there was nothing to commit for this submodule pointer update
            print(f"No changes for submodule: {submodule_name}")
    
    # Check if the HEAD has changed, then push updates
    new_head = repo.head.commit.hexsha
    if original_head != new_head:
        repo.remote().push()
        print("Pushed updated submodule references to remote repository.")
    else:
        print("No updates were made; nothing to push.")

if __name__ == "__main__":
    update_submodules(".")