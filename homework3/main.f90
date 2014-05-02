
program main

    use random_util, only: init_random_seed
    use approx_norm, only: approx_norm1, nsamples

    implicit none
    real(kind=8), allocatable, dimension(:,:) :: a
    real(kind=8) :: colsum, colsum_max, anorm
    integer :: n, seed, i, j

    open(unit=21, file='input_data.txt', status='old')
    read(21,*) n
    read(21,*) seed
    read(21,*) nsamples

    call init_random_seed(seed)  

    ! Create random matrix:
    allocate(a(n,n))
    call random_number(a)

    ! Compute 1-norm as max column sum:
    colsum_max = 0.d0
    do j=1,n
        colsum = 0.d0
        do i=1,n
            colsum = colsum + abs(a(i,j))
            enddo
        colsum_max = max(colsum_max, colsum)
        enddo
            
    ! Estimate 1-norm:
    call approx_norm1(a, anorm)

    print 600, n, colsum_max
600 format("Using matrix with n = ",i5,"   True 1-norm:   ",f16.6)
    print 601, nsamples, anorm
601 format("Based on ",i6," samples, Approximate 1-norm: ",f16.6)

end program main
