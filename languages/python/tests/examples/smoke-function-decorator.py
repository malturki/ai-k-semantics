#defArgs(one, #noIds, {
return 1;
});
#defArgs(two, #noIds, {
return 2;
});
#def(first, f, {
return one;
});
#def(second, f, {
return two;
});
#defDecorated(target, #args(first, #arg(second)), #functionArgs(#noIds, {
return 0;
}));
#call(target, #noArgs);
