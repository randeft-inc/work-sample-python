#! /bin/sh

EXISTING_MSSM_ID=`git config --local user.name`

if [ -z "${EXISTING_MSSM_ID}" ]; then
	echo Generating a new MSSM_ID...
  NEW_MSSM_ID=`cat /dev/urandom | tr -dc '[:alpha:]' | fold -w ${1:-8} | head -n 1`
	git config --local user.name "${NEW_MSSM_ID}"
	git config --local user.email "<>"
else
	echo MSSM_ID already generated.
fi

echo "Your MSSM_ID is: \e[0;34m`git config --local user.name`\e[0m"
echo
