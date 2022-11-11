# http://firsttimeprogrammer.blogspot.bg/2014/09/generate-slope-fields-in-r-and-python.html

# Clear wortkspace
rm(list = ls())

# Clear plots
dev.off(dev.list()["RStudioGD"])

# Get location of current script
fileloc <- dirname(rstudioapi::getSourceEditorContext()$path)

# Set working directory to script location
setwd(fileloc)

# Remove fileloc variable
rm(fileloc)

# Set locale to English
Sys.setlocale("LC_ALL","English")

# Our differential equation
diff <- function(x,y)
{
  return(x-y) #Try also x+y
}

# Line function
TheLine <- function(x1,y1,slp,d)
{
  z = slope*(d-x1)+y1
  return(z)
}

# Domains
x = seq(-20,20,0.5)
y = seq(-20,20,0.5)

# Points to draw our graph
f = c(-5,5) 
h = c(-5,5)
plot(f,h,main="Slope field of y'= x - y", xlab = "", ylab = "")


# Let's generate the slope field
for(j in x)
{
  for(k in y)
  {
    slope = diff(j,k)
    domain = seq(j-0.07,j+0.07,0.14)
    z = TheLine(j,k,slope,domain)
    arrows(domain[1],z[1],domain[2],z[2],length=0.08, col = "red")
  }
}

dev.copy2pdf(file = "fig1.pdf")