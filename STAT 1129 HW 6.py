#!/usr/bin/env r
# coding: utf-8

# In[ ]:


mat1 = matrix(c(7,9,12,2,4,13), nrow=2, ncol=3 ,byrow=TRUE)
mat2 = matrix(c(1,7,12,19,2,8,13,20,3,9,14,21) , nrow=3 ,ncol=4 ,byrow=TRUE)
cat("First Matrix :\n")
print(mat1)
cat("\nSecond Matrix :\n")
print(mat2)
result <- mat1 %*% mat2
cat("\nResulting Matrix :\n")
print(result)


# In[ ]:


#A
id<-c(1,2,3,4,5)
name<-c("Peter","Amy","Ryan","Gary","Michelle")
salary<-c(623.30,515.20,611.00,729.00,843.25)
df<-data.frame(id,name,salary)


# In[ ]:


#B
df$department<-c("IT","finance","computer science","Mathematics","Statistics")


# In[ ]:


#C
df[c(1,3,5),(2,3)]


# In[ ]:


#D
x<-df[c(1,4,5),"salary"]
x
barplot(x,names.arg = c("Peter","Gary","Michelle"),col="red")


# In[ ]:


#E
a=max(salary)
b=min(salary)
c=median(salary)
salary1<-c(a,b,c)
percentage<-round(100*c(a,b,c)/sum(c(a,b,c)))
pie(salary1,main="salary",labels=paste(c("max","min","median"),sep"",percentage,"%"))

