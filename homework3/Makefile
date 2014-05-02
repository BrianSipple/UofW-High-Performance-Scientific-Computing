
OBJECTS = random_util.o approx_norm.o main.o
FFLAGS = -O2

# These flags might be useful for debugging...
#FFLAGS = -g -Wall -fbounds-check -ffpe-trap=zero,overflow,underflow,invalid 

.PHONY: data test clean 

# default values for input_data.txt:
n = 50
seed = 12345
nsamples = 1000

data:
	@echo $(n) > input_data.txt
	@echo $(seed) >> input_data.txt
	@echo $(nsamples) >> input_data.txt
	@echo Wrote data to input_data.txt

test: test.exe data
	./test.exe

test.exe: $(OBJECTS)
	gfortran $(FFLAGS) $(OBJECTS) -o test.exe

%.o : %.f90
	gfortran $(FFLAGS) -c  $< 

clean:
	rm -f *.o *.exe *.mod

