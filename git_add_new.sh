#git add $(git ls-files -o --exclude-standard)

for obj in $(git ls-files -o --exclude-standard); do
    git add $obj
    echo $obj
done

# https://stackoverflow.com/questions/15761890/git-add-only-all-new-files-not-modified-files
