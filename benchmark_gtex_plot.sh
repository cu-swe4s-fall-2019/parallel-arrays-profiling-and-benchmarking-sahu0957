SAMPLE_ATTR=GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
GENE_READS=GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz
GENE=LDLR
GROUP=SMTS
OUTFILE='boxplot.png'
SEARCH='linear'

echo "" > tmp.txt
echo "linear search option time" >> tmp.txt

/home/jovyan/.conda/envs/swe4s/bin/time -f '%e\t%M' python plot_gtex.py \
	--gene_reads $GENE_READS \
	--sample_attributes $SAMPLE_ATTR \
	--gene $GENE \
	--group_type $GROUP \
	--output_file $OUTFILE \
	--search_type $SEARCH >> tmp.txt

echo 'binary search option time' >> tmp.txt
SEARCH='binary'

/home/jovyan/.conda/envs/swe4s/bin/time -f '%e\t%M' python plot_gtex.py \
	--gene_reads $GENE_READS \
	--sample_attributes $SAMPLE_ATTR \
	--gene $GENE \
	--group_type $GROUP \
	--output_file $OUTFILE \
	--search_type $SEARCH >> tmp.txt

echo 'hash table search option time' >> tmp.txt
SEARCH='hash'
/home/jovyan/.conda/envs/swe4s/bin/time -f '%e\t%M' python plot_gtex.py \
	--gene_reads $GENE_READS \
	--sample_attributes $SAMPLE_ATTR \
	--gene $GENE \
	--group_type $GROUP \
	--output_file $OUTFILE \
	--search_type $SEARCH >> tmp.txt

grep 'time' tmp.txt > benchmarking.txt
rm tmp.txt
