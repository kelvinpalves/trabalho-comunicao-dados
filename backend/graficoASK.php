<?php 

require_once 'phplot-6.2.0/phplot.php';

$data = array();
$entrada = str_split($_GET['binario']);

foreach ($entrada as $key => $value) {
    $data[] = $value;
}

$nrz = [];

for ($i = 0; $i < count($data); $i++) {
    $nrz[] = $data[$i] == 0 ? 1 : -1;
}

for ($i = 0; $i < count($data); $i++) {
    $nrz[$i] = $nrz[$i] == -1 ? 0 : $nrz[$i];
}

$dim = count($nrz);

if (count($entrada) == 8) {
    $dim = 16;
}

$va = array();

for ($i = 0; $i < count($nrz); $i++) {
    $f = array_fill(0, $dim, $nrz[$i]);
    $va = array_merge($va, $f);
}

$dim2 = count($va);
$t = linspace(0, count($nrz), $dim2);

$fi = $_GET['frequencia'];

$sinal = 2 * pi() * $fi;

for ($i = 0; $i < count($t); $i++) {
    $t[$i] = $t[$i] * $sinal;
    $t[$i] = sin($t[$i]);
}

$data = array();

for ($i = 0; $i < count($t); $i++) {
    $data[] =  array('', $t[$i] * $va[$i]);
}

$plot = new PHPlot(1000, 150);
$plot->SetImageBorderType('plain');
$plot->SetPlotType('lines');
$plot->SetDataType('text-data');
$plot->SetDataValues($data);
$plot->SetTitle('ASK');
$plot->SetDataColors(array('black'));
$plot->SetLineWidths(1);
$plot->SetDrawXGrid(True);
$plot->SetPlotAreaWorld(0, -1, count($data), 1);
$plot->DrawGraph();

function linspace($i,$f,$n){
    $step = ($f-$i)/($n-1);
    return range ($i,$f,$step);
}
