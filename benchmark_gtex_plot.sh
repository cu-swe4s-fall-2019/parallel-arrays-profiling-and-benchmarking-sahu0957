SAMPLE_ATTR=GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
GENE_READS=GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz
GENE=LDLR
GROUP=SMTS
OUTFILE='boxplot.png'
SEARCH='linear'

echo "" > benchmarking.txt
echo "linear search option time" >> benchmarking.txt

/home/jovyan/.conda/envs/swe4s/bin/time -f '%e\t%M' python plot_gtex.py \
	--gene_reads $GENE_READS \
	--sample_attributes $SAMPLE_ATTR \
	--gene $GENE \
	--group_type $GROUP \
	--output_file $OUTFILE \
	--search_type $SEARCH >> benchmarking.txt

echo 'binary search option time' >> benchmarking.txt
SEARCH='binary'

/home/jovyan/.conda/envs/swe4s/bin/time -f '%e\t%M' python plot_gtex.py \
	--gene_reads $GENE_READS \
	--sample_attributes $SAMPLE_ATTR \
	--gene $GENE \
	--group_type $GROUP \
	--output_file $OUTFILE \
	--search_type $SEARCH >> benchmarking.txt
