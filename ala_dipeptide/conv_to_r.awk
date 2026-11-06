# convert phi/psi map formatted for gnuplot into a matrix suitable for R
# the  phi psi maps are expected in the order
#
#  phi psi energy
#
# with psi being the rapidly varying d.o.f
#
# After a complete pass in psi for a given phi, there should be an empty line
# (i.e., the file should be in the same format as expected by gnuplot)
#

BEGIN {
    phiref=-180;
    full=360;
    idx=0;
    jdx=1;
    minval=1000000;
    ndat=24; # we'll try to get this on the fly, but this serves as a
    incr=full/ndat;  # consistency check.
}

NF==3 {
    idx++;
    enval=$3;
    if (enval<minval) minval=enval;
    ene[idx,jdx]=enval;
    phi=$1;
}

/^\s+$/ || NF==0 {
    nval=idx;
    #print nval;
    if ((phiref != phi)|| (nval != ndat)) {
	print "Warning: we are out of sync" > "/dev/stderr";
	print "Expected phi:", phiref," but got ",phi > "/dev/stderr";
	print "Expected ", ndat," points, got ",nval > "/dev/stderr";
	exit;
    }
#    #printf("! phi =%7.1f\n",phi);
#    for (i=1;i<=nval;i++) {
#	printf("%13.6f",ene[i]);
#	#if (i % 5 == 0) printf("\n");
#    }
    # reset for next iter
#    printf("\n");
    idx=0;
    jdx++;
    phiref+=incr;
}

END {
    #print idx, jdx, minval;
    maxstep = jdx-1;
    for (j=1; j<=maxstep; j++) {
	for (i=1; i<=maxstep; i++) {
	    printf("%10.5f",ene[i,j]-minval);
	}
	printf("\n");
    }
}
