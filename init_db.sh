#!/bin/bash

while [[ $# -gt 0 ]]; do
    case "$1" in
      --user)
      DBUSER="$2"; shift;;
      --db)
      DBNAME="$2"; shift;;
    esac
    shift
done

if [[ -z $DBUSER ]] ; then
  echo "need user"
  exit 0
  elif [[ -z $DBNAME ]] ; then
  echo "need dbname"
  exit 0
else
  psql -U "$DBUSER" -d "$DBNAME" -a -f schema.sql
fi