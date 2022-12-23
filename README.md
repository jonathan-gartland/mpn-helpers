
# mpn-helpers
The following pdf lookup tables collected into a library that could be used in a jupyter notebook perhaps. I copied the values from the pdf's into relatively simple lists of tuples, and then wrote the respective lookup functions. Very simple task that should be OS agnostic and shouldn't need anything to be installed on the users coputer: https://www.idexx.com/en/water/resources/mpn-generator/ 

The Quanti-Tray table values
https://www.idexx.com/media/filer_public/0f/45/0f4542b3-2b85-432b-aa79-e480ce5ad99f/qt51mpntable.pdf

The Quanti-Tray/2000
https://www.idexx.com/media/filer_public/ba/0f/ba0ff3fc-4181-4b34-b9e8-013115d3d011/qt97mpntable.pdf

The Quanti-Tray/Legiolert
https://www.idexx.com/media/filer_public/c9/9b/c99b6023-59fa-4418-95ff-f075ec23962c/quanti-tray-legiolert-mpn-table.pdf  

simply a more convenient way to get the mpn than the company provided windows only application. The bonus for me is that it gives me some practice building a python library for a very low risk task.

how to use:  
in a virtualenv, $>  pip install -i https://test.pypi.org/simple/ mpn-lookup==0.1.0  
$> python  
``` >>> from mpn_lookup import QTArrays  ```  

``` >>> QTArrays.getQTmpn(51) ```  
```['>200.5', 146.1, 'infinite']```  
```>>> ```  

``` >>> QTArrays.getQT2Kmpn(49,48)```  
```['>2419.6', 1439.5, 'infinite']```  
```>>> ```  

``` >>> QTArrays.getQTLEGIOmpn(90, 6) ```  
```'>2272.6'```  
```>>> ```  

This will look up the MPN value from the PDF for the provided positive well count in the first value of the tuple, followed by the 95% low and high confidence values for the .  
