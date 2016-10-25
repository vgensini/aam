C NCLFORTSTART
      SUBROUTINE DAAMOM1(U,DP,LAT,WGT,UMSG,AAM,MLON,NLAT,KLVL)
      IMPLICIT NONE

c NCL:   aam = angmom_atm (u,dp,lat,wgt)

c                                        INPUT
      INTEGER KLVL,NLAT,MLON
      DOUBLE PRECISION U(KLVL,NLAT,MLON),LAT(NLAT),WGT(NLAT),UMSG,
     +                 DP(KLVL)
c                                        OUTPUT
      DOUBLE PRECISION AAM
C NCLEND

c Compute the atmosphere's relative angular momentum

c nomenclature:
c .   u       - zonal wind component (m/s)
c .   dp      - pressure thickness   (Pa)
c.              a 1D array
c .   lat     - latitudes
c .   wgt     - wgts associated with each latitude
c .             These could be gaussian weights or cos(lat)*dlat
c .             where "dlat" is the latitudinal spacing in radians
c .   mlon    - number of longitudes
c .   nlat    - number of latitudes
c .   klvl    - number of levels
c .   umsg    - missing code for "u"
c .   aam     - atmospheric angular momentum [relative]
c .             units: kg*m2/s

c                                        LOCAL
      INTEGER ML,NL,KL
      DOUBLE PRECISION PI,TWOPI,RAD,RE,RE3,G,DLAT,UDP

      PI = 4.0D0*ATAN(1.0D0)
      RAD = PI/180.D0
      TWOPI = 2.0D0*PI

      RE = 6.37122D06
      RE3 = RE**3
      G = 9.81D0
      AAM = 0.0D0

      DO NL = 1,NLAT
c                                     at each latitude
c                                     sum u*dp over all longitudes
          UDP = 0.0D0
          DO ML = 1,MLON
              DO KL = 1,KLVL
                  IF (U(KL,NL,ML).NE.UMSG) THEN
                      UDP = UDP + U(KL,NL,ML)*DP(KL)
                  END IF
              END DO
          END DO
c                                     'zonal average' udp
          UDP = UDP/MLON
c                                     latitudinal contribution to aam
          AAM = AAM + UDP*COS(LAT(NL)*RAD)*WGT(NL)*TWOPI
      END DO

      AAM = (RE3/G)*AAM

      RETURN
      END
c ---------------------------------------------------------