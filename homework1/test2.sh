
# bash script to check for software 
# Insert your name where indicated below.
# Also insert your name where instructed in the file test3.f90.
# Then execute:
#    $ bash test2.sh
# When it looks good, redirect output to a file:
#    $ bash test2.sh > test2output.txt

echo 
echo Code run by  **INSERT YOUR NAME HERE**
echo Environment variable UWHPSC is $UWHPSC
echo Environment variable MYHPSC is $MYHPSC

echo 
echo which ipython returns...
which ipython

echo 
echo which gfortran returns...
which gfortran

echo 
echo gfortran --version returns...
gfortran --version

echo
echo Compiling and running a Fortran code...
gfortran test3.f90
./a.out

