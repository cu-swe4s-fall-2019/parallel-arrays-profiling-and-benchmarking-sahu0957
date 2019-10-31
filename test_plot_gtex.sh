test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

. ssshtest

# Test whether we generate a boxplot
SAMPLE_ATTR=GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
GENE_READS=GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz
GENE=LDLR
GROUP=SMTS
OUTFILE='boxplot.png'
SEARCH='linear'

run linear_search_plot_gtex python plot_gtex.py \
	--gene_reads $GENE_READS \
	--sample_attributes $SAMPLE_ATTR \
	--gene $GENE \
	--group_type $GROUP \
	--output_file $OUTFILE \
	--search_type $SEARCH
assert_exit_code 0

# try running with a bad search parameter
run bad_search_plot_gtex python plot_gtex.py \
	--gene_reads $GENE_READS \
	--sample_attributes $SAMPLE_ATTR \
	--gene $GENE \
	--group_type $GROUP \
	--output_file $OUTFILE \
	--search_type 'foo'
assert_exit_code 1 

run bad_file_plot_gtex python plot_gtex.py \
	--gene_reads 'foo' \
	--sample_attributes $SAMPLE_ATTR \
	--gene $GENE \
	--group_type $GROUP \
	--output_file $OUTFILE \
	--search_type $SEARCH
assert_exit_code 1 

run bad_file_plot_gtex python plot_gtex.py \
	--gene_reads $GENE_READS \
	--sample_attributes 'foo' \
	--gene $GENE \
	--group_type $GROUP \
	--output_file $OUTFILE \
	--search_type $SEARCH
assert_exit_code 1 

SEARCH='binary'

run binary_file_plot_gtex python plot_gtex.py \
	--gene_reads $GENE_READS \
	--sample_attributes $SAMPLE_ATTR \
	--gene $GENE \
	--group_type $GROUP \
	--output_file $OUTFILE \
	--search_type $SEARCH
assert_exit_code 0


SEARCH='hash'

run hash_search_plot_gtex python plot_gtex.py \
	--gene_reads $GENE_READS \
	--sample_attributes $SAMPLE_ATTR \
	--gene $GENE \
	--group_type $GROUP \
	--output_file $OUTFILE \
	--search_type $SEARCH
assert_exit_code 0

run hash_search_plot_gtex_badgroup python plot_gtex.py \
	--gene_reads $GENE_READS \
	--sample_attributes $SAMPLE_ATTR \
	--gene $GENE \
	--group_type 'foo' \
	--output_file $OUTFILE \
	--search_type $SEARCH
assert_exit_code 1
