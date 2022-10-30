# Implementation with 2 patterns

sed -nr '/^[0-9]{3}-[0-9]{3}-[0-9]{4}$|^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$/p' file.txt


# If we merge the similar part, the regex will be like
sed -nr '/(^[0-9]{3}-|^\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/p' file.txt
