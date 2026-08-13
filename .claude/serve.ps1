$port = 8153
$root = "C:\Users\YC Shuchat\Claude work\hebrew-school-of-the-arts"
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")
$listener.Start()
Write-Host "Serving $root on http://localhost:$port/"
while ($listener.IsListening) {
  try {
    $ctx = $listener.GetContext()
    $path = [System.Uri]::UnescapeDataString($ctx.Request.Url.LocalPath.TrimStart('/'))
    if ($path -eq '') { $path = 'index.html' }
    $file = Join-Path $root $path
    if (Test-Path $file -PathType Leaf) {
      $bytes = [System.IO.File]::ReadAllBytes($file)
      $ext = [System.IO.Path]::GetExtension($file).ToLower()
      $ct = switch ($ext) {
        '.html' {'text/html; charset=utf-8'}; '.css' {'text/css; charset=utf-8'}
        '.js' {'application/javascript; charset=utf-8'}
        '.json' {'application/json; charset=utf-8'}; '.webp' {'image/webp'}; '.png' {'image/png'}
        '.jpg' {'image/jpeg'}; '.jpeg' {'image/jpeg'}; '.svg' {'image/svg+xml'}
        '.mp4' {'video/mp4'}; '.pdf' {'application/pdf'}
        '.xml' {'application/xml'}; '.txt' {'text/plain'}; default {'application/octet-stream'}
      }
      $ctx.Response.ContentType = $ct
      $ctx.Response.OutputStream.Write($bytes, 0, $bytes.Length)
    } else {
      $ctx.Response.StatusCode = 404
    }
    $ctx.Response.Close()
  } catch {}
}
