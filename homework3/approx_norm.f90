
module approx_norm

    implicit none
    integer :: nsamples, seed
    save

contains

    subroutine approx_norm1(a, anorm)

    implicit none
    real(kind=8), dimension(:,:), intent(in) :: a
    real(kind=8), intent(out) :: anorm

    anorm = -1.d0   ! this obviously isn't correct

    end subroutine approx_norm1

end module approx_norm
