<?php 

require_once 'phplot-6.2.0/phplot.php';

$data = array();
$entrada = str_split($_GET['binario']);

foreach ($entrada as $key => $value) {
    $data[] = $value;
}

$xs = array();

for ($i = 0; $i <= count($data); $i++) {
    $xs[] = $i;
}

$nzr = [];

for ($i = 0; $i < count($data); $i++) {
    $nzr[] = $data[$i] == 0 ? 1 : -1;
}

$ys = array();

for ($i = 0; $i < count($nzr); $i++) {
    $ys[] = $nzr[$i];
}

$ys[] = $ys[count($ys) -1] == 1 ? 1 : 0;

$xs = array_slice($xs, 1);

$data = array();
for ($i = 0; $i < count($ys); $i++) {
    $data[] = array('', $ys[$i]);
}

$plot = new PHPlot(1000, 150);
$plot->SetImageBorderType('plain');
$plot->SetPlotType('squared');
$plot->SetDataType('text-data');
$plot->SetDataValues($data);
$plot->SetTitle('Codificacao NRZ-L');

$plot->SetDataColors(array('black'));
$plot->SetLineWidths(1);
$plot->SetDrawXGrid(True);
$plot->SetPlotAreaWorld(0, -2, count($data), 2);
$plot->DrawGraph();