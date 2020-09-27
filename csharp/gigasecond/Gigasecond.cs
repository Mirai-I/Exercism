using System;
// https://dobon.net/vb/dotnet/system/datetimecal.html

public static class Gigasecond
{
    public static DateTime Add(DateTime moment)
    {
        TimeSpan giga = new TimeSpan(0,0,0,10^9);
        return moment + giga ;
        
    }
}