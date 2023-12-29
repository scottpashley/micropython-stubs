#!/usr/bin/env pwsh

param(
    [string]$port = "auto",
    [string]$board = "auto",
    [string[]]$version = @("v1.22.0","v1.21.0", "v1.20.0", "v1.19.1" ), #"latest",
    [switch]$force
)
# update the stubs (local ) do not push updates
foreach ($ver in $version) {
    if ($ver -eq "latest" -or $force ) {
        stubber get-docstubs --version $ver
        stubber get-frozen --version $ver
    }
    stubber merge --version $ver --port $port --board $board
    stubber build --version $ver --port $port --board $board
}

