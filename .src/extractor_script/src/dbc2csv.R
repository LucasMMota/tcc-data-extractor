# roda só uma ver na vida pra baixar, depois nao precisa mais
#install.packages("read.dbc")

#ativa a lib
library("read.dbc")

# extractor_script arquivos dbc em csv
dbc2dbf <- function(rawDir, convertedDir, file) {
    # leio o dbc
    x <- read.dbc(paste(rawDir, file, sep=""))
    #escrevo o csv
    write.csv(x, file=paste(convertedDir, file, ".csv", sep=""))
    print(paste('Convertido: ', file))
}

###
args = commandArgs(trailingOnly=TRUE)
# Tests if there are the three needed args: raw dir, converted dir and filename
if (length(args)<3) {
  stop("[(R) dbc2csv] error converting file", call.=FALSE)
}

try(dbc2dbf(args[1], args[2], args[3]), TRUE)