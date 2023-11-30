$ScriptName = $MyInvocation.MyCommand.Name
Write-Host "Starting: '$ScriptName'"

$CurrentDirectory = $PSScriptRoot
Write-Host "The current working directory is: '$CurrentDirectory' ...`n"

# Create an array to hold the results
$results = @()

Get-ChildItem -Path $CurrentDirectory -Recurse -File -Include *.png,*.jpg,*.jpeg | ForEach-Object {
    # Run each Python script and capture the output
    $imageRecOutput = python "ImageRec-2.py" $_.FullName -Verbose
    $imageAlterOutput = python "ImageAlter-2.py" $_.FullName -Verbose
    $imageSearchOutput = python "ImageSearch-2.py" $_.FullName -Verbose

    # Parse outputs to extract the required details
    $crackDamageProb = ($imageRecOutput -match "Is the image a phone with a crack damage\? Probability (\d+.\d+)%" -replace 'Is the image a phone with a crack damage\? Probability ', '').Trim('%')
    $noCrackDamageProb = ($imageRecOutput -match "Is the image a phone with NO crack damage\? Probability (\d+.\d+)%" -replace 'Is the image a phone with NO crack damage\? Probability ', '').Trim('%')
    $iphoneProb = ($imageRecOutput -match "Is the image an iPhone\? Probability (\d+.\d+)%" -replace 'Is the image an iPhone\? Probability ', '').Trim('%')
    $androidProb = ($imageRecOutput -match "Is the image an Android phone\? Probability (\d+.\d+)%" -replace 'Is the image an Android phone\? Probability ', '').Trim('%')
    $imageModified = if($imageAlterOutput -match "has NOT been modified") { "No" } else { "Yes" }
    $imageOriginal = if($imageSearchOutput -match "image is NOT original") { "No" } else { "Yes" }

    # Create a custom object to hold the file results
    $result = [PSCustomObject]@{
        FileName = $_.Name
        CrackDamageProbability = $crackDamageProb
        NoCrackDamageProbability = $noCrackDamageProb
        iPhoneProbability = $iphoneProb
        AndroidProbability = $androidProb
        ImageModified = $imageModified
        ImageOriginal = $imageOriginal
    }

    # Add the results to the array
    $results += $result
}

# Export the results to a CSV file in the current directory
$results | Export-Csv -Path "$CurrentDirectory\Results.csv" -NoTypeInformation

Write-Host "`nImage Analysis Completed. Results have been exported to Results.csv"