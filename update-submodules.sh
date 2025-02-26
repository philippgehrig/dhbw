#!/bin/bash
set -e

# Get list of submodule paths from .gitmodules
submodules=$(git config --file .gitmodules --get-regexp path | awk '{print $2}')

for submodule in $submodules; do
    echo "--------------------------------------------------"
    echo "Processing submodule: $submodule"
    
    # Update the submodule: checkout main and pull the latest commit
    (cd "$submodule" && \
      echo "Checking out main in $submodule..." && \
      git checkout main && \
      echo "Pulling latest changes in $submodule..." && \
      git pull origin main)
    
    # Get the new commit hash of the submodule
    new_hash=$(git -C "$submodule" rev-parse HEAD)
    
    # Stage the updated submodule pointer in the parent repo
    echo "Staging pointer update for $submodule..."
    git add "$submodule"
    
    # Commit the pointer update with a message including submodule name and hash
    commit_message="Update '$submodule' to '$new_hash'"
    echo "Committing with message: $commit_message"
    git commit -m "$commit_message"
    
    # Push the commit to the parent repository
    echo "Pushing update for $submodule..."
    git push
    
    echo "Submodule $submodule updated, committed, and pushed."
done

echo "All submodules updated and parent's repository commits pushed."