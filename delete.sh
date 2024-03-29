find . -type f -name *.pyc -exec rm -rfv {} \;
find . -type f -name *.exe -exec rm -rfv {} \;
find . -type f -name *.out -exec rm -rfv {} \;
find . -type f -name *.so -exec rm -rfv {} \;
find . -type f -name *.exe -exec rm -rfv {} \;
find . -type f -name *.b -exec rm -rfv {} \;
find . -type f -name *.o -exec rm -rfv {} \;
find . -type f -name *.sqlite3 -exec rm -rfv {} \;


# delete executable file 

function delete_exe {
    
    for i in $(find . -type f -not -path "./.git/*" -not -path "*/node_modules/*" ! -name "*.js" ! -name "*.py" ! -name "*.pas" ! -name "*.sh")
    do
        if [[ -x $i ]]
        then
            echo 'exe ' $i
            rm -rfv $i
        fi
            #echo 'no exe ' $i
        #fi
    done

}

delete_exe
