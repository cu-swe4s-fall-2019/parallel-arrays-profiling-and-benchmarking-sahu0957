SAMPLE_ATTR=GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
GENE_READS=GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz
GENE=LDLR
GROUP=SMTS
OUTFILE='boxplot.png'
SEARCH='linear'
echo "" > plot_gtex.linear_search.txt
echo "linear search results" >> plot_gtex.linear_search.txt
python -m cProfile -s tottime plot_gtex.py \
	--gene_reads $GENE_READS \
	--sample_attributes $SAMPLE_ATTR \
	--gene $GENE \
	--group_type $GROUP \
	--output_file $OUTFILE \
	--search_type $SEARCH >> plot_gtex.linear_search.txt

SEARCH='binary'
echo "" > plot_gtex.binary_search.txt
echo "binary search results" >> plot_gtex.binary_search.txt
python -m cProfile -s tottime plot_gtex.py \
	--gene_reads $GENE_READS \
	--sample_attributes $SAMPLE_ATTR \
	--gene $GENE \
	--group_type $GROUP \
	--output_file $OUTFILE \
	--search_type $SEARCH >> plot_gtex.binary_search.txt


SEARCH='hash'
echo "" > plot_gtex.hash_search.txt
echo "hash search results" >> plot_gtex.hash_search.txt
python -m cProfile -s tottime plot_gtex.py \
	--gene_reads $GENE_READS \
	--sample_attributes $SAMPLE_ATTR \
	--gene $GENE \
	--group_type $GROUP \
	--output_file $OUTFILE \
	--search_type $SEARCH | grep -v "hash_and_slot" >> plot_gtex.hash_search.txt
