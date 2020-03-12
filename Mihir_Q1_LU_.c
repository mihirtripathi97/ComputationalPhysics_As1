#include<stdio.h>
#include<stdlib.h>

#include<gsl/gsl_linalg.h>
#include<gsl/gsl_matrix.h>
#include <gsl/gsl_permutation.h>

#include<gsl/gsl_blas.h>





int main()
{
  int i,j,m=3,n=3,s;
  i=j=0;
  double a[3][3]={{1,0.67,0.33},{0.45,1,0.55},{0.67,0.33,1}};

  gsl_matrix *A,*L,*U,*A_p;
  A = gsl_matrix_calloc(m,n);
  A_p = gsl_matrix_calloc(m,n);
  L = gsl_matrix_calloc(m,n);
  gsl_matrix_set_identity(L);
  U = gsl_matrix_calloc(m,n);
  gsl_permutation * p = gsl_permutation_alloc (3);
  gsl_permutation_init (p);

  for (i = 0; i < m; i += 1)
  for (j = 0; j < n; j += 1)

  gsl_matrix_set(A,i,j,a[i][j]);



  printf("\nInput Matrix A\n\n");
  for (i = 0; i < m; i += 1)
  {
      for (j = 0; j < n; j += 1)
      {
          printf("%f ",gsl_matrix_get(A,i,j));
      }
        printf("\n");
  }


  //LU decomposition
 gsl_linalg_LU_decomp(A, p,&s);

  for (i = 0; i < m; i += 1)
  {
     for (j = 0; j < n; j += 1)
     {
     	       if(i>j)
     	  gsl_matrix_set(L,i,j,gsl_matrix_get(A,i,j));


     	       if(i<=j)
     	  gsl_matrix_set(U,i,j,gsl_matrix_get(A,i,j));

     }
  }
  printf("\nLower triangular Matrix\n\n");
  for (i = 0; i < m; i += 1)
  {
      for (j = 0; j < n; j += 1)
      {
          printf("%f ",gsl_matrix_get(L,i,j));
      }
      printf("\n");
  }

  printf("\nUpper triangular\n\n");
  for (i = 0; i < m; i += 1)
  {
      for (j = 0; j < n; j += 1)
      {
          printf("%f ",gsl_matrix_get(U,i,j));
      }
        printf("\n");
  }


gsl_blas_dgemm (CblasNoTrans, CblasNoTrans,1.0,L,U,0.0,A_p);

  printf("\nMatrix LU\n\n");
   for (i = 0; i < m; i += 1)
  {for (j = 0; j < n; j += 1)
      {  printf("%f ",gsl_matrix_get(A_p,i,j));
        }
        printf("\n");}

  return 0;
}

