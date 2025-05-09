# example_api

### Usage:
example_api [-h] _modelInfoFile_ _fingerPrintImage_

### Output:
If example_api is able to parse both an NFIQ 2 model and fingerprint image, the expected output will be a list of native quality measures generated from the fingerprint image. These are the same native quality measures that can be obtained from the NFIQ 2 CLI CSV output.

Each native quality measure will be printed with its respective header. Each native quality measure will be printed on a separate line.

The first value that printed is the unified quality score and it will appear as:

	"UnifiedQualityScore: [value]"

The next series of values will be from actionable feedback. This includes `"EmptyImageOrContrastTooLow: [value]"` to `"SufficientFingerprintForeground: [value]"`.

The final series of values will be native quality measures. These are the values generated by the individual native quality measures that comprise the NFIQ 2 unified quality score. This includes `"FDA_Bin10_0: [value]"` to  `"RVUP_Bin10_StdDev: [value]"`.

### Testing

Expected output files are located in the "output" directory. To ensure that scores generated by the sample API are consistent with the expected output, you can perform a diff on the two outputs.

```bash
$ diff SFinGe_Test_0X_output.txt Your_SFinGe_Test_0X_output.txt
```

If the resulting output is empty, then the generated scores are identical.

### Citation

The fingerprint images included in the `images` subdirectory are synthetic images generated by SFiNGe[1] .

[1] Cappelli, R., Maio, D., and Maltoni, D. SFinGe: An Approach to Synthetic Fingerprint Generation, International Workshop on Biometric Technologies, 2004. (Demo software available at http://biolab.csr.unibo.it/research.asp?organize=Activities&select=&selObj=12&pathSubj=111%7C%7C12& ).
